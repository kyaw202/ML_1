How to Push to GitHub Repository Using SSH
Generate an SSH Key (if you don't have one): If you don’t have an SSH key, generate one using the following command:

bash
Copy code
ssh-keygen -t ed25519 -C "your_email@example.com"
When prompted for the file location, press Enter to save the key at the default location (~/.ssh/id_ed25519).
When prompted for a passphrase, you can either:
Enter a passphrase (for added security), or
Leave it empty and press Enter for no passphrase.
Add Your SSH Key to the SSH Agent: Ensure your SSH key is added to the SSH agent with the following commands:

bash
Copy code
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
Add Your Public SSH Key to GitHub:

Copy the public key to your clipboard:
bash
Copy code
pbcopy < ~/.ssh/id_ed25519.pub
Go to GitHub's SSH and GPG keys section.
Click New SSH key, give it a title, and paste the copied key.
Set Up the Correct Remote URL:

Check the remote URL:
bash
Copy code
git remote -v
If it shows an HTTPS URL (e.g., https://github.com/kyaw202/ML-in-Prod-batch-1.git), you need to update it to use SSH.
To update the URL, run:
bash
Copy code
git remote set-url origin git@github.com:kyaw202/ML_1.git
Replace kyaw202/ML_1.git with the correct repository name.
Verify the Remote URL: Run the following command to ensure the URL is correctly set:

bash
Copy code
git remote -v
The output should now look like:

plaintext
Copy code
origin  git@github.com:kyaw202/ML_1.git (fetch)
origin  git@github.com:kyaw202/ML_1.git (push)
Push Your Changes: Finally, push your local changes to the GitHub repository:

bash
Copy code
git push
If this is your first push, or if you’re pushing a new branch, you may need to specify the branch name:

bash
Copy code
git push origin main
Troubleshooting Tips:
"Permission denied (publickey)" Error:

Make sure your public SSH key is added to your GitHub account under Settings > SSH and GPG keys.
Confirm the key is loaded into the SSH agent using:
bash
Copy code
ssh-add -l
If no key is listed, run:
bash
Copy code
ssh-add ~/.ssh/id_ed25519
"Repository not found" Error:

Double-check that the repository exists on GitHub and that you have the correct access rights (write access).
Ensure the remote URL is correct by running git remote -v.