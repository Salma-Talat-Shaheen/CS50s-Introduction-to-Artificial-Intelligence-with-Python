# Degrees of Separation — Find the Shortest Path Between Actors

## Project Overview

This project is inspired by the *Six Degrees of Kevin Bacon* game, where the goal is to find the shortest path of connections between two actors, with each connection representing a movie both actors starred in. Using **Breadth-First Search (BFS)**, we will calculate the minimum number of "degrees of separation" between two actors.

### Python Version
- **Recommended Python version**: Python 3.12

### Objective
Write a Python program that calculates how many “degrees of separation” two actors are apart by finding the shortest path between them using BFS.

---

## Problem Background

In the *Six Degrees of Kevin Bacon* game, all actors can be connected to Kevin Bacon within six steps, where each step is a movie that two actors have starred in together. The objective of this project is to find the shortest connection (path) between any two actors using shared movies.

**Example**:
- Jennifer Lawrence → *X-Men: First Class* → Kevin Bacon → *Apollo 13* → Tom Hanks  
- This results in **2 degrees of separation**.

The task is to find a similar path for any pair of actors.

---

## Data

The project includes CSV files containing information about actors, movies, and their co-stars:

1. **people.csv**:
   - Contains actor details (id, name, birth year).

2. **movies.csv**:
   - Contains movie details (id, title, year).

3. **stars.csv**:
   - Contains relationships between actors and movies (person_id, movie_id).

---

## Structure of the Code

### Data Structures

1. **names**:  
   Maps actor names to a set of corresponding person_ids (to handle duplicate names).
   
2. **people**:  
   Maps person_id to a dictionary containing the actor’s name, birth year, and the set of movies they have starred in.
   
3. **movies**:  
   Maps movie_id to a dictionary containing the movie's title, year, and the set of stars who appeared in it.

4. **neighbors_for_person(person_id)**:  
   Returns a set of `(movie_id, person_id)` pairs for all the actors who starred in the same movie as the given actor (person_id).

---

## Specifications

### Required Functions:

1. **`shortest_path(source, target)`**:
   - **Input**: `source`, `target` (actor names).
   - **Output**: A list of `(movie_id, person_id)` tuples showing the shortest path from `source` to `target`.
   - If no path exists, return `None`.
   - If multiple paths of equal length exist, return any valid path.
   - Use **Breadth-First Search (BFS)** to find the shortest path.

2. **`neighbors_for_person(person_id)`**:
   - Given a `person_id`, returns a set of `(movie_id, person_id)` pairs for all people who starred in a movie with the given person.

### Program Flow

1. **Data Loading**:
   - Load data from CSV files into dictionaries (`names`, `people`, `movies`).
   
2. **User Interaction**:
   - Prompt the user to input two actor names.
   - Retrieve the actor IDs using the `person_id_for_name` function.
   
3. **Find Path**:
   - Call `shortest_path` to find the shortest path between the two actors.

4. **Output**:
   - Display the degree of separation and the movies linking the actors.

---

## Example

Suppose you run the program with the names "Emma Watson" and "Jennifer Lawrence":

```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class

