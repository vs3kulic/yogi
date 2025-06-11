// Define types based on your Django models

export interface YogaClass {
  id: number;
  name: string;
  yoga_type: YogaType;
  class_type: string;
  key_features: string | null;
  ideal_for: string;
}

export type YogaType = 'Burnout-Yogini' | 'Ashtanga-Warrior' | 'Homeoffice-Yogini' | 'Casual-Stretcher';

// Extend window interface for yogaData
declare global {
  interface Window {
    yogaData?: {
      classes?: YogaClass[];
      result_type?: YogaType | '';
    }
  }
}

// API response types
export interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}

export interface ApiError {
  message: string;
  status: number;
}

// Event types for type safety when emitting events
export interface FilterChangeEvent {
  type: YogaType | '';
}

export interface ClassSelectEvent {
  yogaClass: YogaClass;
}