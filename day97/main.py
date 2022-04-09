from checklastdaygithub import CheckLastDayGitHubBot

USER_GITHUB = "filipehlreis"

if __name__ == "__main__":
    github = CheckLastDayGitHubBot(USER_GITHUB)
    commit_level = github.get_last_day_github()
    github.send_sms_github(commit_level)
