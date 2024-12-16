import React, {useState, useEffect} from 'react'
import Movie from '../Movie/Movie'

export const Home = (username) => {
    const [movies, setMovies] = useState([])
    const [movie, setMovie] = useState()

    console.log('usernam eis', username)
  
    useEffect(() => {
  
      const fetchAndPick = async () => {
        const fetched = await fetchMovies();
        pickMovie(fetched);
      }
      fetchAndPick()
    }, [])
  
    const fetchMovies = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/movies')
      const data = await response.json()
      setMovies(data.movies)
      console.log(data.movies)
      return data.movies
    }
  
    const pickMovie = (fetched) => {
      const randomPick = Math.floor(Math.random() * fetched.length)
      setMovie(fetched[randomPick])
      console.log("Movie:", fetched[randomPick].title)
  
    }
  
    return <Movie movie = {movie}/>
}
