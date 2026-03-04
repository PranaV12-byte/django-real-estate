import axios from "axios";

const API_URL = "/api/v1/auth/";

// Register user
const register = async (userData) => {
    const response = await axios.post(API_URL + "users/", userData);

    return response.data;
};

// Login user
const login = async (userData) => {
    const response = await axios.post(API_URL + "jwt/create/", userData);

    if (response.data) {
        localStorage.setItem("user", JSON.stringify(response.data));
    }

    return response.data;
};

// Logout user
const logout = () => {
    localStorage.removeItem("user");
};

// Activate user
const activate = async (userData) => {
    const response = await axios.post(API_URL + "users/activation/", userData);

    return response.data;
};

const authService = {
    register,
    logout,
    login,
    activate,
};

export default authService;
