const film = {
    judul: "Interstellar",
    tahunRilis: 2014,
    sutradara: "Christopher Nolan",
    genre: ["Sci-Fi", "Adventure", "Drama"],

    tampilkanDetail: function() {

        return `Judul: ${this.judul}, Tahun Rilis: ${this.tahunRilis}, Sutradara: ${this.sutradara}, Genre: ${this.genre.join(', ')}`;
    }
};

console.log("Nilai properti sutradara: - main.js:13", film.sutradara);
console.log("Nilai elemen kedua dalam properti genre: - main.js:14", film.genre[1]);
console.log("Hasil pemanggilan method tampilkanDetail: - main.js:15", film.tampilkanDetail());