import { createRouter, createWebHistory } from "vue-router";
import Editor from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Editor,
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/RegisterUser"),
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
