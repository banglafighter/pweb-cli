from git import Repo
from ppy_common import Console
from ppy_file_text import FileUtil


class PWebGitRepo:

    @staticmethod
    def get_repo_name_from_url(url: str):
        if not url:
            return None

        last_slash_index = url.rfind("/")
        last_suffix_index = url.rfind(".git")
        if last_suffix_index < 0:
            last_suffix_index = len(url)

        if last_slash_index < 0 or last_suffix_index <= last_slash_index:
            raise Exception("Invalid repo url {}".format(url))

        return url[last_slash_index + 1:last_suffix_index]

    @staticmethod
    def clone_or_pull_project(path, url, branch):
        try:
            repo_name = PWebGitRepo.get_repo_name_from_url(url)
            if not repo_name:
                raise Exception("Invalid repo")
            if not FileUtil.is_exist(path):
                Console.success("Cloning project: " + repo_name + ", Branch: " + branch)
                Repo.clone_from(url, branch=branch, to_path=path)
            else:
                Console.success(repo_name + " Taking pull...")
                repo = Repo(path)

                repo.remotes.origin.fetch()
                local_branch_name = repo.active_branch.name

                Console.info("Local branch name : " + local_branch_name + ", Checkout branch: " + str(branch))

                if local_branch_name != branch:
                    repo.git.checkout(branch)
                origin = repo.remotes.origin
                origin.pull()
        except Exception as e:
            print("\n\n")
            Console.error(f"Git Exception {str(e)}")
