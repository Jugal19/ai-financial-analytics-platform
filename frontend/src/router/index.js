import { createRouter, createWebHistory } from 'vue-router'

// Pages
import Dashboard from '../pages/Dashboard.vue'
import Analytics from '../pages/Analytics.vue'
import Assistant from '../pages/Assistant.vue'
import Settings from '../pages/Settings.vue'

const routes = [
    { path: '/', redirect: '/dashboard' },
    { path: '/dashboard', component: Dashboard },
    { path: '/analytics', component: Analytics },
    { path: '/assistant', component: Assistant },
    { path: '/settings', component: Settings },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router