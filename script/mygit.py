import git
from common import MyFile

class MyGitManager:
    def __init__(self, repo_path="", branch_name="", changelog=""):

        if MyFile.IsDirExist(repo_path) and MyFile.IsFileExist(changelog):
            self.repo_path, self.branch_name, self.push_time = self.get_repo_info(repo_path, branch_name)
            self.changelog = MyFile.find_first_versions_in_file(changelog)

        else:
            ret1 = MyFile.IsDirExist(repo_path)
            ret2 = MyFile.IsFileExist(changelog)
            self.repo_path = "https://github.com/Jun-red/ImageAnalysis.git"
            self.branch_name = "ui_dev"
            self.changelog = "0.0.3"



    def get_repo_info(self, repo_path, branch_name):
        repo = git.Repo(repo_path)
        url = repo.remotes.origin.url if repo.remotes else None
        branch = repo.branches[branch_name]
        latest_commit = branch.commit
        latest_commit_time = latest_commit.authored_datetime  # 获取提交的时间
        return url ,branch, latest_commit_time
        # url,_, latest_commit_time = get_repo_info(repo_path, branch_name)
        # print("Url:", url)
        # print("branch:", _)
        # print("Latest commit time:", latest_commit_time)

