import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      "/api/inference": {
        target: "https://router.huggingface.co",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/inference/, ""),
      },
    },
  },
});
