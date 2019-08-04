from script_scraper import ScriptScraper


def run_script_scraper(tv_scripts, script_letters, site_url, thread_count, download_directory):
  # Initialize the "Springfield, Springfield" screen scraper
  scraper = ScriptScraper(tv_scripts,
                          script_letters,
                          site_url,
                          thread_count,
                          download_directory
                         )

  scraper.scrape_site()

if __name__ == '__main__':
  # Parameters for scraping scripts from "Springfield, Springfield" site
  tv_scripts = True
  script_letters = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z']
  site_url = 'https://www.springfieldspringfield.co.uk'
  thread_count = 4
  download_directory = 'test'

  # Engage!
  run_script_scraper(tv_scripts, script_letters, site_url, thread_count, download_directory)
