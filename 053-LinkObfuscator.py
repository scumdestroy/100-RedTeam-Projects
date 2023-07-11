# The Less than Fascinating Origins, Transformation and Powerful Conclusive Iteration of the URL-Swamping-
# Note, I wrote a weak and disappointing script that just stored URLs you send in a log and sends you encryped output.
# and then if you want to decypher it, you send it back to the server, and get your original URL back.  Yes, I agree, pretty useless.  Also insecure and stupid, as it just stores the unencrypted values in plain text on the server.
# So I go to post it here and start writing excuses, like, I know that it sucks but guys!! I'd need like my own server.. and domain... and process requests for remote connections ...and upon writing all that out, 
# I realized it is extremely within my reasonable capabilities, even to the level of hosting it and giving it one of the random domain names I horde for a few dollars per year.  
# It is esentially just like bit.ly, but without an interface, that can only really be accessed via curl or other command-line spawned POST request with JSON data as a body payload.

import http.server
import json
import random
import string
import urllib.parse
import argparse

class RequestHandler(http.server.BaseHTTPRequestHandler):
    server_domain = ''  # Replace with your server's domain
    deception_words = ['pray', 'holy', 'spirit', 'wisdom', 'glory', 'grace', 'redemption', 'service', 'charity',
                       'doves', 'lambs', 'beauty', 'jews', 'muslim', 'arab', 'allah', 'rejoice', 'pray', 'priesthood',
                       'nunforge', 'prosperity', 'judah', 'psalms', 'shadows', 'faith', 'hebrews', 'safety',
                       'mourning', 'slaughter', 'trouble', 'thorncrown', 'crucifix', 'vampyre', 'desecration',
                       'rites', 'darkness', 'demonic', 'hands', 'puncture', 'funerary', 'funeral', 'scorn', 'decimation',
                       'immolation', 'annihilation', 'incantation', 'occultism', 'okkulto', 'straightedge', 'sxe',
                       'madball', 'americafirst', 'patriot', 'winningbig', 'pray', 'pray', 'wolf', 'slut', 'renewed',
                       'raped', 'stimulated', 'masturbatory', 'grinning', 'skinless', 'headless', 'bloody', 'pig',
                       'tyrant', 'massacre', 'butchery', 'vomitory', 'primitive', 'diealone', 'bold', 'seeker',
                       'sickness', 'toxicity', 'biohazard', 'nuclear', 'undertaker', 'coffin', 'grave', 'cremetory',
                       'crimes', 'suffocate', 'assault', 'rifleman', 'sniper', 'grenadier', 'accelerationist',
                       'antigoth', 'deadcommunists', 'helicopters', 'motorhead', 'adultbaby', 'filthy', 'pornographic',
                       'mature', 'stained', 'stripped', 'husks', 'broken', 'torture', 'gardens', 'genocide', 'organs',
                       'white', 'houses', 'black', 'nooses', 'slaves', 'grindcore', 'power', 'violence', 'super',
                       'general', 'colonel', 'recruits', 'casualties', 'collateral', 'larceny', 'theft', 'burglary',
                       'siphon', 'circuits', 'hacked', 'chunks', 'rebuke', 'rescind', 'descent']

    obfuscated_urls = {}  # Stores the mapping of obfuscated URLs to original URLs

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            request_json = json.loads(post_data.decode('utf-8'))
            url = request_json.get('url', '')
            deception = request_json.get('deception', '')

            obfuscated_url = self.obfuscate_url(url, deception)
            self.obfuscated_urls[obfuscated_url] = url  # Store the mapping of obfuscated URL to original URL

            response_data = {
                'message': 'Greetings, my friend. Your noble task has been processed and approved.',
                'original_url': url,
                'obfuscated_url': obfuscated_url
            }
            response_body = json.dumps(response_data).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(response_body)))
            self.end_headers()
            self.wfile.write(response_body)
        except json.JSONDecodeError as e:
            print(f'Error decoding JSON payload: {e}')
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', '0')
            self.end_headers()

    def do_GET(self):
        if self.path in self.obfuscated_urls:
            original_url = self.obfuscated_urls[self.path]
            self.send_response(302)
            self.send_header('Location', original_url)
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', '0')
            self.end_headers()

    def obfuscate_url(self, url, deception):
        parsed_url = urllib.parse.urlparse(url)
        cleaned_deception = self.clean_deception(deception)
        if cleaned_deception:
            path = f'/{cleaned_deception}'
        else:
            path = '/' + '-'.join(random.sample(self.deception_words, 2))

        random_string = self.generate_random_string()
        obfuscated_path = f'{path}/{random_string}'

        obfuscated_url = urllib.parse.urlunparse(parsed_url._replace(netloc=self.server_domain, path=obfuscated_path))
        return obfuscated_url

    def clean_deception(self, deception):
        if not deception:
            return ''

        cleaned_deception = ''.join(c if c.isalnum() else '-' for c in deception)
        return cleaned_deception

    def generate_random_string(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def log_obfuscated_url(self, original_url, obfuscated_url):
        # Implement your logging mechanism here
        with open('obfuscated_urls.log', 'a') as log_file:
            log_file.write(f'{obfuscated_url} : {original_url}\n')
        print(f'Original URL: {original_url}')
        print(f'Obfuscated URL: {obfuscated_url}')

def start_server
