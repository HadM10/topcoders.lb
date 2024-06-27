# PORTFOLIO
### LTK Work Soft 2024

#### Install Dependencies
> 1. Go to the official Python website: Visit [python.org](https://www.python.org/downloads/)
> 2. Download Python
> 3. Run the installer
> 4. Verify installation `python --version` or `python3 --version`
> 5. Install extensions
> ```bash
>   pip install flask # web framework
>   pip install gunicorn # Python WEB SERVER GATEWAY INTERFACE (WSGI) HTTP Server for UNIX systems.
> ```
> 6. [Jinja2 documentation](https://jinja.palletsprojects.com/en/3.1.x/)
> 7. [flask documentation](https://flask.palletsprojects.com/en/3.0.x/)
#### Content
> * static
>   * css
>   * fonts
>   * images
>   * js
>   * sass
>   * cv.pdf
> * templates
>   * components
>     * about.html
>     * contacts.html
>     * education.html
>     * hero.html
>     * sidebar.html
>     * skills.html
>     * stats.html
>     * what_i_do.html
>     * work.html
>   * index.html
> * .gitignore
> * app.py # create and run the application
> * data.py # the data used in the index
> * Procfile # file used for heroku
> * README.md
> * requirements.txt
>   * to generate requirements file: command → `pip freeze > requirements.txt`

### Run the application
#### 1- Development Mode (in app.py)
```python
...
# change the debug to True
if __name__ == '__main__':
    app.run(debug=True)
```
#### 2- Production Mode (in app.py)
```python
...
# change the debug to False
if __name__ == '__main__':
    app.run(debug=False)
```
#### Command to run in terminal
```shell
python run.py
```
#### !important
> Always change debug to False for production mode