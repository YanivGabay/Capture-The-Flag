## level 4

so its basicly the same drill, but now we need to use docker compose to run a docker
on the GCE (google cloud env) VM
the same code for level 3 , no additional changes.
first we created the PAT (person access token) into github, and uploaded and tagged our docker package 
so we can easily acess it from or VM.
the youtube tutorial was super helpful on creating a PAT and tagging and pushing it into our git.
the package is located on my personal github:
[YanivGabay GitHub](https://github.com/YanivGabay?tab=packages)

after that, the "tricky" part, was to install docker on our VM which i choose debian
but after a few commands and a few stackoverflow to understand why docker was installed and not
docker compose, i succsefully installed it.


althourgh its bad to share this, cause it is limited to 7 days i did write the token here:
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
