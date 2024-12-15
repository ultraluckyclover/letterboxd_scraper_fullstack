import React from "react";

const Movie = ({movie}) => {
    if (!movie) {
        return <p>Loading...</p>
    }
    console.log(movie.title)
    return (
        <div>
            <h2>{movie.title}</h2>
            <h2>{movie.releaseYear}</h2>
            <img src = {movie.imgUrl}></img>
        </div>
    )
}

export default Movie



// return (<div>
    //     <h2>Movies</h2>
    //     <table>
    //         <thead>
    //             <tr>
    //                 <th>Title</th>
    //                 <th>Release Year</th>
    //             </tr>
    //         </thead>
    //         <tbody>
    //             {movies.map(movie => (
    //                 <tr key = {movie.id}>
    //                     <td>{movie.title}</td>
    //                     <td>{movie.releaseYear}</td>
    //                 </tr>
    //             ))}
    //         </tbody>
    //     </table>
    // </div>)