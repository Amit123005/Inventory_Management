import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New React Router App" },
    { name: "description", content: "Welcome to React Router!" },
  ];
}
export default function Home() {
  return (
    <div className="max-w-4xl mx-auto mt-12 p-6 bg-white shadow rounded-xl">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome Home</h1>
      <p className="text-gray-600">This is the homepage of your app.</p>
    </div>
  );
}

