import requests
import datetime
import os

def load_env_file(filepath=".env"):
    if not os.path.exists(filepath):
        return
    with open(filepath) as f:
        for line in f:
            # Remove whitespace and skip comments/empty lines
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            
            # Split by the first '=' found
            key, value = line.split("=", 1)
            os.environ[key] = value

load_env_file()

# CONFIG
GITHUB_TOKEN = os.getenv("GITHUB_API_KEY")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
API_URL = "https://api.github.com/repos/{}/{}/commits"

# array of students with name, username, repository 
students = [
    {"name": "Alan", "username": "ayeoh-aca", "repo": "AP-CSP"},
    {"name": "Kiki", "username": "kikibb08", "repo": "aca_cs"},
    {"name": "Westin", "username": "WestinBledsoe", "repo": "aca_ap_cs"},
    {"name": "Sean", "username": "dingawasoo", "repo": "aca_ap_cs"},
    {"name": "George", "username": "TheCh0sen0ne-boop", "repo": "ap_cs"},
    {"name": "Henry", "username": "henrylipscomb-source", "repo": "ap_cs"},
    {"name": "Miles", "username": "miles-mcneese-aca", "repo": "ap-csp"},
    {"name": "Devin", "username": "devin881", "repo": "school"},
    {"name": "Bryce", "username": "jamesherndon-cell", "repo": "aca_ap_cs"},
    {"name": "Finley", "username": "finleylove-wq", "repo": "web-project"},
    {"name": "MJ", "username": "MJM1213", "repo": "main"},
    {"name": "Norah", "username": "norahstanfill", "repo": "ap_cs"},
    {"name": "Ginger", "username": "virginiarespess-lang", "repo": "ap_cs"},
    {"name": "Sam", "username": "samuelvestal-del", "repo": "APcomp_sci"},
    {"name": "Tim", "username": "TimSvoboda112", "repo": "Timot1"},
    {"name": "William", "username": "wwickstrum", "repo": "WWAPCS"},
    {"name": "Wade", "username": "WADECOLEMAN", "repo": "wc_aca_stuff"},
    {"name": "Lyndi", "username": "no-pal", "repo": "acacs"},
    {"name": "Hayden", "username": "Hayden-21", "repo": "ApCompSci"},
    {"name": "Melanie", "username": "melanieguerreromedina-ai", "repo": "Heeelo"},
    {"name": "Nash", "username": "GR3ATB0B", "repo": "aca-website"},
]


def get_latest_commit(user, repo):
    try:
        # get only most recent commit
        url = API_URL.format(user, repo)
        response = requests.get(url, headers=HEADERS, params={"per_page": 1})
        
        if response.status_code == 200:
            data = response.json()
            if not data:
                return "No commits found"
            
            commit = data[0]
            author_date = commit['commit']['author']['date']
            message = commit['commit']['message']
            
            # format date
            dt_obj = datetime.datetime.strptime(author_date, "%Y-%m-%dT%H:%M:%SZ")
            formatted_date = dt_obj.strftime("%Y-%m-%d %H:%M")
            
            # calculate lapsed time
            now = datetime.datetime.utcnow()
            delta = now - dt_obj
            days_ago = delta.days + 1
            
            return {
                "date": formatted_date,
                "days_ago": days_ago,
                "message": message.split('\n')[0][:50]  # truncate long messages
            }
        elif response.status_code == 404:
            return "Repo Not Found"
        else:
            return f"Error: {response.status_code}"
            
    except Exception as e:
        return f"Exception: {str(e)}"

def main():
    now_formatted = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    print(f"{'STUDENT':<10} | {'DAYS AGO':<12} | {'DATE ('+now_formatted+')':<8} | {'MESSAGE'}")
    print("-" * 80)
    
    for student in students:
        result = get_latest_commit(student['username'], student['repo'])
        
        name_display = student['name'][:19]
        
        if isinstance(result, dict):
            # highlight students who haven't pushed in > 1 day (24hours)
            days_display = f"{result['days_ago']} days"
            if result['days_ago'] > 1:
                days_display += " (!)"
                
            print(f"{name_display:<10} | {days_display:<12} | {result['date']:<16} | {result['message']}")
        else:
            # Error state
            print(f"{name_display:<10} | {'N/A':<12} | {'N/A':<16} | {result}")

if __name__ == "__main__":
    main()