class ConversationMemory:
#this class is used to store the conversation memory and the workflowof the conversation
    def __init__(self):
        # -------------------------
        # Product Memory
        # -------------------------
        self.selected_product = None
        self.last_products = []

        # -------------------------
        # User Memory
        # -------------------------
        self.current_user = None

        # User information collected
        # before calling create_user()
        self.pending_user = {
            "name": None,
            "email": None,
            "phone": None,
        }

        # -------------------------
        # Order Memory
        # -------------------------
        self.pending_order = None

        # -------------------------
        # Conversation State
        # -------------------------
        self.state = "idle"

    # ==========================================
    # Product
    # ==========================================
#this function is used to select the and stores to the conversation state 

    def set_selected_product(self, product):
        self.selected_product = product

    def get_selected_product(self):
        return self.selected_product

    def set_last_products(self, products):
        self.last_products = products

    def get_last_products(self):
        return self.last_products

    # ==========================================
    # User
    # ==========================================
#this function is used to collect the user query and store it in the conversation state
#if the user is already logged in it will the database and get the user information and stored it
#if the user is new it will collect the user details and store it
    def set_current_user(self, user):
        self.current_user = user

    def get_current_user(self):
        return self.current_user

    # Pending User

    def set_pending_name(self, name):
        self.pending_user["name"] = name

    def set_pending_email(self, email):
        self.pending_user["email"] = email

    def set_pending_phone(self, phone):
        self.pending_user["phone"] = phone

    def get_pending_user(self):
        return self.pending_user

    def clear_pending_user(self):
        self.pending_user = {
            "name": None,
            "email": None,
            "phone": None,
        }

    # ==========================================
    # Order
    # ==========================================
#this function is used to collect the order details and store it in the conversation state    

    def set_pending_order(self, order):
        self.pending_order = order

    def get_pending_order(self):
        return self.pending_order

    def clear_pending_order(self):
        self.pending_order = None

    # ==========================================
    # State
    # ==========================================    
#this function is used to set the state of the conversation and get the state of the conversation
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    # ==========================================
    # Clear Everything
    # ==========================================

    def clear(self):
        self.selected_product = None
        self.last_products = []

        self.current_user = None

        self.pending_user = {
            "name": None,
            "email": None,
            "phone": None,
        }

        self.pending_order = None

        self.state = "idle"