# How to create a local branch and push it to the origin

## Cloning the repo to local drive
The followig command will clone the repo from the link provided into the directory you are currently in, Creating a new directoy in the current one for the repo.
```PowerShell
git clone https://github.com/ConorMcCabe29/university-access.git
```
## Creating a branch in the local repo
This command will create a new branch and the -b is to give the new branch a name and what follows is the name set for the branch.
After creating the local branch you need to move the file to the directory of the repo in local.
```PowerShell
git checkout -b addMarkDownExample
```
## Checking what changes you've made
This is for checking the status of what changes you've made. 
```PowerShell
git status
```
## Add a file to the branch
Use the following to add the file in the directory to what will be committed.
The ./ Is for the Windows OS ./ Is up directory in Unix based OS.
```PowerShell
git add ./NAME_OF_FILE_HERE
```

## Add a commit for your changes
```PowerShell
 git commit -m "Add how to write markdown example"
 ```
 
## Push the local branch into the origin
This will push the local branch into the origin to create a pull request.
```PowerShell
 git push --set-upstream origin addMarkDownExample
 ```
 
