# Setup

1. Install Python 3.5+
2. Install requirements using: `pip install -r requirements.txt`
3. Enter the `src` folder with `cd src`
4. Create database & apply migrations: `python manage.py migrate`
5. Run development server with `python manage.py runserver`

## API

### Examples

#### Get list of users (requires superuser authentication)

`GET /api/1.0/users`

#### Create an user

```
POST /api/1.0/users
{
  "username": "mscott",
  "first_name": "Michael",
  "last_name": "Scott",
  "email": "mscott@dundermifflin.com",
  "password": "ilovepaper"
}
```

#### Delete an user (requires superuser or authentication)

`DELETE /api/1.0/users/<id>`

#### Get user details (requires authentication)

`GET /api/1.0/users/<id>`

#### Get list of blogs

`GET /api/1.0/blogs`

  - *Optional*: Search by name (`?name=<term>`)
  - *Optional*: Order by `username` (`?ordering=username`)

#### Get list of posts in a blog (requires authentication for drafts)

`GET /api/1.0/blogs/<name>`

  - *Optional*: Search by title and content (`?search=<term>`)
  - *Optional*: Order by `published_at` or `title` (`?ordering=<choice>`)

#### Get post details (requires authentication for drafts):

`GET /api/1.0/posts/<id>`

#### Delete post (requires authentication)

`DELETE /api/1.0/posts/<id>`

#### Create post (requires authentication)

```
POST /api/1.0/posts/create
{
  "title": "My first post",
  "abstract": "This is my first post",
  "image": "http://some-url.com/image.jpg",
  "body": "Lorem ipsum..."
}
```
