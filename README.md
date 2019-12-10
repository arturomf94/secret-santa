Secret Santa! :)

# How to use:

**0** Set up your environment variables in a file `.env` to contain the following:

  - MY_ADDRESS="myaddress"
  - PASSWORD="mypwd"
  - HOST="myhost" 
  - PORT="myport"
  
Host and port depend on your service provider. e.g. for gmail: smtp.gmail.com and 587.

**1** Create a `contacts.txt` with the contact details of all the people involved. For instance: 

```bash
name1 address1@mail.com
name2 address2@mail.com
```

**2** Create a `message.txt` in `html` format that contains the values `${PERSON_NAME}`, `${GIVES_TO}`, so as to say that `${PERSON_NAME}` has been assigned to give gifts to `${GIVES_TO}`. 

```bash
<pre>
Hey ${PERSON_NAME}!

You were assigned the following person: ${GIVES_TO} 🎄

</pre>
```
**3** Place these files under `docs/`

**4** Create and activate a virtual environment for the project: 

```bash
virtualenv venv
source venv/bin/activate
```
**5** Install the requirements:

```bash
pip install -r requirements.txt
```

**6** Run the script:

```bash
python src/main.py
```
