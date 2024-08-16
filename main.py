import gzip
import shutil
import os
import argparse
import json
from rich.console import Console
from rich.table import Table

class Extractor:
    def __init__(self, input_file, output_dir=None, eip='extracted.txt', host=None):
        self.input_file = input_file
        self.output_dir = output_dir if output_dir else os.path.dirname(input_file)
        self.output_file = os.path.join(self.output_dir, os.path.basename(input_file).replace('.gz', ''))
        self.eip = eip
        self.host = host
        self.table = Table()
        self.table.add_column("IP Address", style="cyan")
        self.table.add_column("Port", style="red")
        self.table.add_column("Hostname", style="yellow")
        self.console = Console()


    def Banner(self):
        self.holders = """
           _____ __              __               ______     __                  __            
          / ___// /_  ____  ____/ /___ _____     / ____/  __/ /__________ ______/ /_____  _____
          \__ \/ __ \/ __ \/ __  / __ `/ __ \   / __/ | |/_/ __/ ___/ __ `/ ___/ __/ __ \/ ___/
         ___/ / / / / /_/ / /_/ / /_/ / / / /  / /____>  </ /_/ /  / /_/ / /__/ /_/ /_/ / /    
        /____/_/ /_/\____/\__,_/\__,_/_/ /_/  /_____/_/|_|\__/_/   \__,_/\___/\__/\____/_/      v1.0.5

                                                                    by 0xAgun
        """

        print(self.holders)

    
    def extract(self):
        if not os.path.exists(self.input_file):
            print(f"Error: {self.input_file} does not exist.")
            return
        
        try:
            with gzip.open(self.input_file, 'rb') as f_in:
                with open(self.output_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f"File extracted successfully to {self.output_file}")
        except Exception as e:
            print(f"Failed to extract {self.input_file}. Error: {e}")
    
    def read_content(self):
        try:
            with open(self.output_file, 'r') as file:
                self.content = file.read()
        except Exception as e:
            print(f"Failed to read content from {self.output_file}. Error: {e}")
    
    def extract_ip_and_port(self):
        results = []
        hosts = []
        try:
            with open(self.output_file, 'r') as file:
                content = file.read()
                json_objects = content.strip().split('\n')
                for obj in json_objects:
                    try:
                        contest = json.loads(obj)
                        ip_str = contest.get('ip_str')
                        port = contest.get('port')
                        hostnames = contest.get('hostnames', [])
                        if ip_str and port:
                            results.append(f"{ip_str}:{port}")
                            hosts.append(hostnames)
                            self.table.add_row(str(ip_str), str(port), ', '.join(hostnames))
                    except json.JSONDecodeError as e:
                        print(f"JSON decode error: {e}")
            
            with open(self.eip, 'w') as file:
                for result in results:
                    file.write(result + '\n')

            if self.host:
                with open(self.host, 'w') as file:
                    for sublist in hosts:
                        for item in sublist:
                            file.write(item + '\n')

            self.console.print(self.table)
        except Exception as e:
            print(f"Failed to extract IP and port. Error: {e}")

    def get_output_file(self):
        return self.output_file

def main():
    parser = argparse.ArgumentParser(description="Extract  the .gz shodan file and parse ip port hostnames")
    parser.add_argument("input_file", type=str, help="Path to the .gz file to be extracted")
    parser.add_argument("-o", "--output_dir", type=str, default=None, help="Directory to extract the file to")
    parser.add_argument("-e", "--eip", type=str, default='extracted.txt', help="File to save extracted IP and port")
    parser.add_argument("-H", "--host", type=str, default=None, help="File to save extracted hostnames")

    args = parser.parse_args()

    extractor = Extractor(args.input_file, args.output_dir, args.eip, args.host)
    extractor.Banner()
    extractor.extract()
    extractor.read_content()
    extractor.extract_ip_and_port()

if __name__ == "__main__":
    main()
