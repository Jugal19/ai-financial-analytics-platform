<template>
    <div class="bg-gray-900 rounded-xl p-6 border border-gray-800 hover:border-indigo-500 transition">
        <p class="text-sm text-gray-400">{{ title }}</p>
        <h2 class="text-2xl font-bold mt-2">{{ value }}</h2>

        <div class="mt-3 text-xs text-green-400">+12% this month</div>
    </div>
</template>

<script setup>
    defineProps({
        title: String,
        value: String
    })
</script>