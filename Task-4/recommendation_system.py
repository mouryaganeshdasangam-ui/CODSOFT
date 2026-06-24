import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings("ignore")

movies_data = {
    "title": ["The Dark Knight", "Inception", "Interstellar", "The Avengers", "Iron Man", 
              "The Notebook", "Titanic", "La La Land", "Toy Story", "Finding Nemo"],
    "features": ["Action Crime Thriller Batman fights the Joker", 
                 "Action Sci-Fi Thriller A thief enters dreams", 
                 "Adventure Drama Sci-Fi Astronauts travel through a wormhole",
                 "Action Adventure Sci-Fi Superheroes save Earth", 
                 "Action Adventure Sci-Fi Inventor builds armored suit", 
                 "Drama Romance Love story from different backgrounds",
                 "Drama Romance Love story on a ship", 
                 "Comedy Drama Romance Musician and actress fall in love", 
                 "Animation Adventure Comedy Toys come to life",
                 "Animation Adventure Comedy Clownfish searches for lost son"]
}

books_data = {
    "title": ["1984", "Brave New World", "The Hobbit", "Harry Potter", "Lord of the Rings",
              "Pride and Prejudice", "Romeo and Juliet", "The Great Gatsby", "To Kill a Mockingbird", "Dune"],
    "features": ["Dystopian Sci-Fi Totalitarian regime surveillance",
                 "Dystopian Sci-Fi Genetically engineered society",
                 "Fantasy Adventure A hobbit goes on a quest",
                 "Fantasy Magic A young wizard goes to school",
                 "Fantasy Adventure Fellowship destroys a ring",
                 "Romance Classic Elizabeth Bennet and Mr. Darcy",
                 "Romance Tragedy Two star-crossed lovers",
                 "Classic Fiction Wealth and tragedy in the 1920s",
                 "Classic Fiction Racism and justice in the South",
                 "Sci-Fi Space Desert planet and giant worms"]
}

products_data = {
    "title": ["iPhone 15", "Samsung Galaxy S24", "MacBook Pro", "Dell XPS 15", "Sony WH-1000XM5",
              "AirPods Pro", "Kindle Paperwhite", "iPad Air", "Nintendo Switch", "PlayStation 5"],
    "features": ["Smartphone Apple iOS Camera 5G",
                 "Smartphone Android AI Camera 5G",
                 "Laptop Apple M3 Chip Performance",
                 "Laptop Windows OLED Performance",
                 "Headphones Sony Noise Cancelling Wireless",
                 "Earbuds Apple Noise Cancelling Wireless",
                 "E-Reader Amazon E-Ink Reading",
                 "Tablet Apple Touchscreen Productivity",
                 "Gaming Console Nintendo Handheld Mario",
                 "Gaming Console Sony 4K Performance"]
}

def create_recommender(data_dict):
    df = pd.DataFrame(data_dict)
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["features"])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return df, similarity_matrix

def recommend(item_title, df, similarity_matrix, top_n=3):
    matches = df[df["title"].str.lower() == item_title.lower()]
    if matches.empty:
        print(f"\nItem '{item_title}' not found in the database.")
        return
    
    item_index = matches.index[0]
    similarity_scores = list(enumerate(similarity_matrix[item_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    top_similar = similarity_scores[1:top_n + 1]
    
    print(f"\nRecommendations based on '{matches.iloc[0]['title']}':")
    for idx, score in top_similar:
        print(f"- {df.iloc[idx]['title']}")

if __name__ == "__main__":
    datasets = {
        "1": ("Movies", *create_recommender(movies_data)),
        "2": ("Books", *create_recommender(books_data)),
        "3": ("Products", *create_recommender(products_data))
    }

    print("=" * 45)
    print("      UNIVERSAL RECOMMENDATION SYSTEM")
    print("=" * 45)
    
    while True:
        print("\nCategories:")
        print("1. Movies")
        print("2. Books")
        print("3. Products")
        print("4. Exit")
        
        choice = input("\nSelect a category (1-4): ").strip()
        
        if choice == '4':
            print("Goodbye!")
            break
            
        if choice in datasets:
            category_name, df, sim_matrix = datasets[choice]
            print(f"\nAvailable {category_name}:")
            print(", ".join(df["title"].tolist()))
            
            user_input = input(f"\nEnter a {category_name[:-1].lower()} you like: ").strip()
            if user_input:
                recommend(user_input, df, sim_matrix)
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
