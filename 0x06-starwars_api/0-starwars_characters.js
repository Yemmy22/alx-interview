#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Helper function to make request and return a promise
function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchCharacters () {
  try {
    // Get movie data
    const movieResponse = await fetch(url);
    const characters = JSON.parse(movieResponse).characters;

    // Fetch character names in order
    const characterNames = await Promise.all(
      characters.map(async (characterUrl) => {
        const characterResponse = await fetch(characterUrl);
        return JSON.parse(characterResponse).name;
      })
    );

    // Print each character name in the correct order
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error(error);
  }
}

fetchCharacters();
