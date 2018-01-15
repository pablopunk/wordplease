# Setup

1. Install Python 3.5+
2. Install requirements using: `pip install -r requirements.txt`
3. Enter the `src` folder with `cd src`
4. Create database & apply migrations: `python manage.py migrate`
5. Run development server with `python manage.py runserver`

## API

### Examples

* Get list of users

`GET /api/1.0/users`

* Get user details (requires authentication)

`GET /api/1.0/users/<id>`

* Get list of blogs

`GET /api/1.0/blogs`

* Get list of posts in a blog (requires authentication for drafts)

`GET /api/1.0/blogs/<name>`

* Create post (requires authentication)

`POST /api/1.0/posts/create`

* Get post details (requires authentication for drafts):

`GET /api/1.0/posts/<id>`
