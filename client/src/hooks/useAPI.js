import useSWR from "swr";

// Simple fetch function
const fetcher = (...args) => fetch(...args).then((res) => res.json());

export function useAPI(path) {
  // Prefix the path with /api
  const apiPath = `/api${path}`;
  return useSWR(apiPath, fetcher);
}
