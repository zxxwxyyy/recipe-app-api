# Recipe App API

This is a Recipe App API built with Django Rest Framework and Docker. It's a test-driven development project that provides functionalities for managing users and recipes.

## Features

- User registration and authentication (token-based)
- User profile management
- Recipe management (create, retrieve, update, delete)
- Recipe filtering based on tags and ingredients
- Image uploading for recipes

## Models

- `User`: Custom user model that uses email for authentication.
- `Recipe`: Model for storing recipe data. Each recipe is associated with a user and can have multiple tags and ingredients. Recipes can also have an image.
- `Tag`: Model for storing tag data. Each tag is associated with a user.
- `Ingredient`: Model for storing ingredient data. Each ingredient is associated with a user.

## API Endpoints

- `/api/user/create/`: Create a new user.
- `/api/user/token/`: Obtain a token for a user.
- `/api/user/me/`: Retrieve and update the authenticated user.
- `/api/recipe/recipes/`: Create a new recipe or retrieve existing recipes.
- `/api/recipe/recipes/<id>/`: Retrieve, update, or delete a specific recipe.
- `/api/recipe/recipes/<id>/upload_image/`: Upload an image for a specific recipe.
- `/api/recipe/tags/`: Retrieve existing tags.
- `/api/recipe/ingredients/`: Retrieve existing ingredients.

## Setup

This project uses Docker, so make sure Docker is installed on your machine. To get started, clone the repository and then run:

```bash
docker-compose up
