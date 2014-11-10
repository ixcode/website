# SSH Mysteries

So we want to set up a user for our server that can be for example used by our build tool or ansible.

It wants to have a different ssh key than our personal one, so we need to create a new key, upload it to the server and then use it to ssh in.

## Create the key

I store all the keys in my home account on my local machine. Replace 'username' with the name of the use ron the target machine.

mkdir ~/.ssh/username

cd ~/.ssh/username

ssh-keygen -t rsa -b 2048 -f ~/.ssh/username/id_rsa -C "username@host or whatever comment you like"

Copy it up there...

cat ~/.ssh/username/id_rsa.pub | ssh username@host 'cat - >> ~/.ssh/authorized_keys'

And now login.

ssh -i ~/.ssh/<username>/id_rsa username@host

Now I found that I had to login first and create the .ssh/authorized_keys. If you have to do this, make sure you set the file permissions correctly

chmod 0700 ~/.ssh/
chmod 0600 ~/.ssh/authorized_keys

I discovered this the hard way and was able to use the '-v' flag in the ssh command to find out that the permissions were incorrectly set:

ssh -v -i ~/.ssh/<username>/id_rsa username@host