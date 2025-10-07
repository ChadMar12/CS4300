# Cinetix - Movie Theater Booking Application

A RESTful Movie Theater Booking Application built with Python and Django that integrates with The Movie Database (TMDB) API.

# Render Host
https://cinetix-vqow.onrender.com/

## Features

The application allows users to:
- View movie listings via the API
- Book seats via the API
- Check their booking history via the API
- Use an attractive user interface built with Django templates and Bootstrap that displays and manipulates the same data as the API

## About Cinetix

Cinetix is a demo movie theater booking application created for Homework 2. The app allows you to browse through movies using The Movie Database (TMDB) API and pulls all types of films using a dropdown selector:
- Now Playing
- Popular
- Top Rated
- Upcoming

## Getting Started

### Prerequisites

- Python 3.12.6 or higher
- pip or conda package manager

### Installation

#### Step 1: Clone the Repository

First, clone the repository to your local machine.

#### Step 2: Create a Virtual Environment

**Using venv:**

```bash
python -m venv .venv
source venv/bin/activate
```

**Using conda:**

```bash
conda create --name myenv python=3.12.6
conda activate myenv
```

#### Step 3: Install Dependencies

Install all required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Application

Once you have installed the requirements, run the application using one of the following commands:

**Standard command:**

```bash
python -m gunicorn movie_theater_booking.asgi:application -k uvicorn.workers.UvicornWorker
```

**Alternative command (if the standard command doesn't work):**

```bash
python -m gunicorn movie_theater_booking.asgi:application \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --workers 1 \
  --timeout 120
```

This will force the application to load on port 8000. If you want to change the port number, modify the `--bind 0.0.0.0:8000` line.

The server should start up locally, and you will be able to browse and book movies from TMDB.

## Design Process

### Design Tools

The design of the model and API was created using **Figma** to structure and design the layout of each webpage. After creating the designs, the base background for each HTML and CSS file was built. For more complex features, ChatGPT and Claude AI were utilized for development assistance.

**Figma Design Files:** [View on Figma](https://www.figma.com/site/W1A5ib0TNAWDOraxgcItTQ/homework-2?t=xjvrhkJnp2QWjJgk-6)

### AI Assistance Breakdown

**ChatGPT:**
- Page formatting
- Movie poster animations
- Seat array for dynamically creating movie theaters
- Ideas for connecting frontend to backend

**Claude AI:**
- JavaScript booking script that connects to the database
- Landing page feature films
- Ideas for connecting frontend to backend

### Design Inspiration

Design inspiration was drawn from websites like:
- Fandango
- Cinemark

## Assets & Credits

### User Profile Picture
- Source: [Smashicons on Flaticon](https://www.flaticon.com/authors/smashicons)

### Cinetix Logo
- Designer: @socialadvizer designs on Canva

### Feature Films

1. **One Battle After Another**
   - Website: https://www.onebattleafteranothermovie.com/

2. **Demon Slayer: Kimetsu no Yaiba Infinity Castle-Sub**
   - Source: https://megaplex.com/film/HO00003870/demon-slayer-kimetsu-no-yaiba-infinity-castle-sub

3. **Gabby's Dollhouse: The Movie**
   - Source: https://megaplex.com/film/HO00003917/gabbys-dollhouse-the-movie

## License

This project was created as part of Homework 2.

## 🌟 Acknowledgements

* Django Documentation
* TMDB API
* Bootstrap
* Inspiration: Fandango & Cinemark

## Support

For issues or questions, please refer to the project documentation or contact the development team.
