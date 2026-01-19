import re

SKILLS = ['python', 'django', 'sql', 'html', 'css', 'javascript', 'react']

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if re.search(r'\b' + skill + r'\b', text)]

def match_score(job_skills, user_skills):
    job = set(job_skills.lower().split(','))
    user = set(user_skills.lower().split(','))

    if not job:
        return 0

    return int(len(job & user) / len(job) * 100)
