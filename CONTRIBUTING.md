# Contributing to silas

Below are the guidelines for contributing to silas. Follow these steps so you don't break anything.

1. Open an issue for any code you want to add. Label the issue with whatever is appropriate.
2. Clone the repository or run `git pull` in the repository to pull the latest changes from `master`.
3. Create a new branch for the code being added using `git checkout -b your-branch-name`. For enhancement issues, begin branch names with `add` and for bug issues, begin branch names with `fix`. Keep branch names short.
4. Create your code.
5. Make sure to keep your branch consistent with `master` by running `git rebase master` within the branch.
6. Add changes made to files using `git add file-name`. Make sure that you are in your own branch, and not `master`.
7. Commit changes using `git commit -m "[your commit message]"`. Commit messages should be short and summarize major changes.
8. Push your changes to your branch using `git push origin your-branch-name`.
9. On GitHub, Open a Pull Request from your branch. The body of the pull request should be a single line `Fixes #[issue number]`. This makes it so that when the pull request is merged, the corresponding issue is automatically closed.