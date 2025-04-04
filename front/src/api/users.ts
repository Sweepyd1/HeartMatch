import apiClient from './axios';
import type { UserType } from '@/models/user';


export const UserApi = {
  getAllUsers: async () => {
    return await apiClient.get('/users');
  },

  getUserById: async (id: string) => {
    return await apiClient.get(`/users/${id}`);
  },

  createUser: async (userData: UserType) => {
    return await apiClient.post('/users', userData);
  },

  updateUser: async (id: string, userData: Partial<UserType>) => {
    return await apiClient.patch(`/users/${id}`, userData);
  },

  deleteUser: async (id: string) => {
    return await apiClient.delete(`/users/${id}`);
  },
  getProfileInfo: async (user_id:Number) =>{
    return await apiClient.get('/get_profile_info')
  }
};


