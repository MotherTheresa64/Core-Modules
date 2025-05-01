# 1. Configure Git (only needed once per machine)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 2. Initialize a Git repo
git init

# 3. Create a sample file and add it
touch index.html
git add index.html
git commit -m "Initial commit with index.html"

# 4. Create a new branch and switch to it
git branch feature-branch
git checkout feature-branch

# 5. Make a new change in this branch
touch feature.txt
git add feature.txt
git commit -m "Add feature.txt in feature-branch"

# 6. Switch back to main and merge the feature branch
git checkout main
git merge feature-branch

# 7. Link to a remote GitHub repo (replace the URL with your actual one)
git remote add origin https://github.com/your-username/your-repo-name.git

# 8. Push your changes
git push -u origin main
