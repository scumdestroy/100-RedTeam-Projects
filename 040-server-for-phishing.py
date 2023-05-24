import requests
import os

def clone_website(url):
    response = requests.get(url)
    
    clone_dir = 'cloned_website'
    if not os.path.exists(clone_dir):
        os.makedirs(clone_dir)
    
    base_url = url.split('//')[-1].split('/')[0]
    
    with open(os.path.join(clone_dir, 'index.html'), 'wb') as file:
        file.write(response.content)
    
    # Clone additional linked resources (CSS, JS, images, etc.)
    for resource in response.iter_content():
        resource_url = resource.get('href') or resource.get('src')
        if resource_url and base_url in resource_url:
            resource_url = resource_url.replace(base_url, '')
            resource_path = os.path.join(clone_dir, resource_url.lstrip('/'))clone 
            os.makedirs(os.path.dirname(resource_path), exist_ok=True)
            
            resource_response = requests.get(url + resource_url)
            with open(resource_path, 'wb') as file:
                file.write(resource_response.content)
    
    print("Website cloned successfully!")
    
def log_post_requests(url):
    #log all POST requests
    while True:
        data = {}
        print("Enter data to send (press 'q' to quit):")
        key = input("Key: ")
        
        if key == 'q':
            break
        
        value = input("Value: ")
        data[key] = value
        
        response = requests.post(url, data=data)
        
        with open('post_requests_log.txt', 'a') as file:
            file.write(f"POST Request - URL: {url}, Data: {data}\n")
        
        print("POST request sent and logged!")
    

if __name__ == '__main__':
    website_url = input("Enter the website URL to clone: ")
    
    clone_website(website_url)
    
    log_post_requests(website_url)
