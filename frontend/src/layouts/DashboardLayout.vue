<template>
    <div class="flex min-h-screen bg-gray-900 text-gray-100">
        <Sidebar />

        <div class="flex flex-col flex-1">
            <Topbar />

            <main class="p-6">
                <router-view />
            </main>
        </div>
    </div>
</template>

<script setup>
    import Sidebar from '../components/Sidbar.vue'
    import Topbar from '../components/Topbar.vue'
</script>