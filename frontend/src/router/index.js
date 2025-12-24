import { createRouter, createWebHistory } from 'vue-router'

import Dashbaord from '../pages/Dashboard.vue'
import Analytics from '../pages/Analytics.vue'
import Assistant from '../pages/Assistant.vue'
import Settings from '../pages/Settings.vue'

const routes = [
    { path: '/', redirect: '/dashboard' },
    { path: '/dashboard', component: Dashbaord },
    { path: '/analytics', component: Analytics },
    { path: '/assistant', component: Assistant },
    { path: '/settings', component: Settings},
]

export default createRouter({
    history: createWebHistory(),
    routes,
})