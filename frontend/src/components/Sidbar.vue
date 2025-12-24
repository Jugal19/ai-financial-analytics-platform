<template>
    <aside class="w-64 bg-gray-900 p-6 border-r border-gray-800 hidden md:block">
        <h2 class="text-xl font-bold mb-10">AI Finance</h2>

        <nav class="space-y-3 text-sm">
            <router-link to="/dashboard" class="block px-3 py-2 rounded hover:bg-gray-800" 
                active-class="bg-gray-800 text-white">
                Dashboard
            </router-link>

            <router-link to="/analytics" class="block px-3 py-2 rounded hover:bg-gray-800"
                active-class="bg-gray-800 text-white">
                Analytics
            </router-link>

            <router-link to="/assistant" class="block px3 py-2 rounded hover:bg-gray-800"
                active-class="bg-gray-800 text-white">
                AI Assistant
            </router-link>

            <router-link to="/settings" class="block px-3 py-2 rounded hover:bg-gray-800"
                active-class="bg-gray-800 text-white">
                Settings
            </router-link>
        </nav>
    </aside>
</template>