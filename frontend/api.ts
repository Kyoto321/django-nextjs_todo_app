import { ITask } from "./types/tasks";

const baseUrl = 'http://localhost:8000/api';

export const getAllTodos = async (): Promise<ITask[]> => {
  const res = await fetch('http://localhost:8000/api/users/dashboard', { cache: 'no-store' });
  const todos = await res.json();
  return todos;
}

export const addTodo = async (todo: ITask): Promise<ITask> => {
  const res = await fetch(`http://localhost:8000/api/users/create-task`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(todo)
  })
  const newTodo = await res.json();
  return newTodo;
}

export const editTodo = async (todo: ITask): Promise<ITask> => {
  const res = await fetch(`http://localhost:8000/api/users/update/<slug:slug>/${todo.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(todo)
  })
  const updatedTodo = await res.json();
  return updatedTodo;
}

export const deleteTodo = async (id: string): Promise<void> => {
  await fetch(`http://localhost:8000/api/users/delete/<slug:slug>/${id}`, {
    method: 'DELETE',
  })
}