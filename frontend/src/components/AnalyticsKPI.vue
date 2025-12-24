<template>
    <div class="bg-gray-900 border border-gray-800 rounded-xl p-5">
        <p class="text-sm text-gray-400">{{ label }}</p>
        <p class="text-2xl font-bold mt-2">{{ value }}</p>
        <p v-if="subtitle" class="text-xs text-gray-500 mt-1">{{ subtitle }}</p>
    </div>
</template>

<script setup>
    defineProps({
        label: String,
        value: String,
        subtitle: String
    })
</script>