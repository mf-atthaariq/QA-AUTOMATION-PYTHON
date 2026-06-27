class ApiRoutes:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # Sentralisasi endpoint ala Enterprise Pattern
    POSTS = f"{BASE_URL}/posts"
    USERS = f"{BASE_URL}/users"
    
    @staticmethod
    def get_post_by_id(post_id: int) -> str:
        return f"{ApiRoutes.POSTS}/{post_id}"