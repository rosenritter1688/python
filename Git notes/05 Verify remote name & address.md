
##Verify remote name / address
`git remote -v`

```shows in console
$git remote -v
myOrigin ssh://git@example.com:1234/myRepo.git (fetch)
myOrigin ssh://git@example.com:1234/myRepo.git (push)

# this will fail because `origin` is not set
$git push origin master

# you need to use
$git push myOrigin master
```