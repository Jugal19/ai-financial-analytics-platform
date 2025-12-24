<template>
    <div
        class="max-w-xl px-4 py-3 rounded-lg text-sm"
        :class="isUser
            ? 'ml-auto big-indigo-600 text-white'
            : 'mr-auto bg-gray-800 text-gray-100 border border-gray-700'"
    >
        {{ message }}
    </div>
</template>

<script setup>
    defineProps({
        message: String,
        isUser: Boolean,
    })
</script>