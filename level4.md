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
than it was easy as pie, upload the docker compose file with the ssh online terminal
docker compose up, and we had our machine running a docker with our image and running our code
and found the flag!

### 9.9 update
we were asked to automate most of the task
so first i need to add SSH key to my VM in gce, so i can "talk" with her locally using a shell script

created a ssh rsa key:

```bash
ssh-keygen -t rsa -b 2048 -f .ssh/my_gce_key  
```

add the SSH key to the machine in the metadate section
DONT FORGET TO SAVE!!!!

if the key is not read only, it will not allow us to connect.
in linux we would use chmod but were on windows so were using:

```powershell
Get-ItemProperty -Path ".\my_gce_key" | Select-Object IsReadOnly
Get-ItemProperty -Path ".\my_gce_key.pub" | Select-Object IsReadOnly
```

now we can connect to the machine with the following

```bash
ssh -i ./.ssh/my_gce_key username@externalip
```

althourgh its bad to share this, cause it is limited to 7 days i did write the token here:
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
