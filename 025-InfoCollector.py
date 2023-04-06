import argparse
import requests
import bs4

def main(query, num_results):
    # Search on Google, Bing, and Yahoo
    results = {}
    for engine in ['google', 'bing', 'yahoo']:
        if engine == 'yahoo':
            search_url = f"https://search.yahoo.com/search?p={query}"
        else:
            search_url = f"https://www.{engine}.com/search?q={query}"
        results[engine] = scrape_search_results(search_url, num_results)

    # Summarize the results
    print(f"Top {num_results} results for '{query}':")
    for engine, links in results.items():
        print(f"\n{engine.capitalize()}:")
        for i, link in enumerate(links):
            print(f"{i+1}. {link}")

def scrape_search_results(url, num_results):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = []
    for i, result in enumerate(soup.select('.r a')):
        if i == num_results:
            break
        links.append(result.get('href'))
    return links

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search a query on Google, Bing, and Yahoo.')
    parser.add_argument('query', help='The query to search.')
    parser.add_argument('--num-results', type=int, default=5,
                        help='The number of results to show for each search engine.')
    args = parser.parse_args()

    main(args.query, args.num_results)
