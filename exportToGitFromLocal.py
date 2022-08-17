#import github 
from github import Github

#create github instance
g = Github("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")

#repo name
GITHUB_REPO = "new_rep"

repo = g.get_user().get_repo('{0}'.format(GITHUB_REPO))

# get file names from git repo
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))


#read file you want to upload

file_name = 'KingsCrownBOA1 [0.0].xml'
with open(file_name, 'r') as file:
    content = file.read()

# Upload to github
git_prefix = 'model/' #folder name
git_file = git_prefix + file_name

#check if git file already exists, if already exists update the file , if not create new
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="main")
    print(git_file + ' CREATED')