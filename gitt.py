import git
from git import Repo, exc

def git_commit_details():

    sanity_dictionary = {}
    repo1 = '/home/ubuntu/server/repo1'
    repo2 = '/home/ubuntu/server/repo2'
    repo3 = '/home/ubuntu/server/repo3'
    repo4 = '/home/ubuntu/server/repo4'

    repo = git.Repo(repo1)
    commit = repo.head.commit

    if not repo.head.is_detached:
        branch = repo.active_branch.name
    else:
        branch = "Detached HEAD"

    sha = commit.hexsha
    author_name = commit.author.name
    author_email = commit.author.email
    commit_date = commit.authored_datetime
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    try:
        latest_tag = repo.git.describe(commit, contains=True)
    except exc.GitCommandError as e:
        if "fatal: cannot describe" in str(e):
            latest_tag = None
        else:
            # Handle other GitCommandError exceptions
            raise e


    sanity_dictionary["Branch repo1"] = branch
    sanity_dictionary["Commit ID repo1"] = sha
    sanity_dictionary["Commit Author repo1"] = author_name, "<" + author_email + ">"
    sanity_dictionary["Commit Date repo1"] = formatted_date
    sanity_dictionary["Commit Tag repo1"] = latest_tag if latest_tag else "Not Tagged"

    repo = git.Repo(repo2)
    commit = repo.head.commit

    if not repo.head.is_detached:
        branch = repo.active_branch.name
    else:
        branch = "Detached HEAD"

    sha = commit.hexsha
    author_name = commit.author.name
    author_email = commit.author.email
    commit_date = commit.authored_datetime
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    try:
        latest_tag = repo.git.describe(commit, contains=True)
    except exc.GitCommandError as e:
        if "fatal: cannot describe" in str(e):
            latest_tag = None
        else:
            # Handle other GitCommandError exceptions
            raise e


    sanity_dictionary["Branch repo2"] = branch
    sanity_dictionary["Commit ID repo2"] = sha
    sanity_dictionary["Commit Author repo2"] = author_name, "<" + author_email + ">"
    sanity_dictionary["Commit Date repo2"] = formatted_date
    sanity_dictionary["Commit Tag repo2"] = latest_tag if latest_tag else "Not Tagged"

    sanity_dictionary.update(sanity_dictionary)

    repo = git.Repo(repo3)
    commit = repo.head.commit

    if not repo.head.is_detached:
        branch = repo.active_branch.name
    else:
        branch = "Detached HEAD"

    sha = commit.hexsha
    author_name = commit.author.name
    author_email = commit.author.email
    commit_date = commit.authored_datetime
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    try:
        latest_tag = repo.git.describe(commit, contains=True)
    except exc.GitCommandError as e:
        if "fatal: cannot describe" in str(e):
             latest_tag = None
        else:
            # Handle other GitCommandError exceptions
            raise e


    sanity_dictionary["Branch repo3"] = branch
    sanity_dictionary["Commit ID repo3"] = sha
    sanity_dictionary["Commit Author repo3"] = author_name, "<" + author_email + ">"
    sanity_dictionary["Commit Date repo3"] = formatted_date
    sanity_dictionary["Commit Tag repo3"] = latest_tag if latest_tag else "Not Tagged"


    sanity_dictionary.update(sanity_dictionary)

    repo = git.Repo(repo4)
    commit = repo.head.commit

    if not repo.head.is_detached:
        branch = repo.active_branch.name
    else:
        branch = "Detached HEAD"

    sha = commit.hexsha
    author_name = commit.author.name
    author_email = commit.author.email
    commit_date = commit.authored_datetime
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    try:
        latest_tag = repo.git.describe(commit, contains=True)
    except exc.GitCommandError as e:
        if "fatal: cannot describe" in str(e):
            latest_tag = None
        else:
            # Handle other GitCommandError exceptions
            raise e

    sanity_dictionary["Branch repo4"] = branch
    sanity_dictionary["Commit repo4"] = sha
    sanity_dictionary["Commit Author repo4"] = author_name, "<" + author_email + ">"
    sanity_dictionary["Commit Date repo4"] = formatted_date
    sanity_dictionary["Commit Tag repo4"] = latest_tag if latest_tag else "Not Tagged"


    sanity_dictionary.update(sanity_dictionary)

    print (sanity_dictionary)
    return sanity_dictionary


if __name__ == "__main__":
    git_commit_details()
