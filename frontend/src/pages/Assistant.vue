<template>
    <div class="max-w-7x1 mx-auto space-y-6">
        <div class="flex flex-col min-h[70vh]">
            <!-- Page Header -->
            <div class="mb-4">
                <h2 class="text-2xl font-bold">AI Assistant</h2>
                <p class="text-gray-400 text-sm">Ask questions about your finances and trends</p>
            </div>

            <!-- Chat Area -->
            <div class="flex-1 overflow-y-auto bg-gray-900 border border-gray-800 rounded-xl p-4 space-y-4">
                
                <!-- Empty State -->
                <div 
                    v-if="messages.length === 0" 
                    class="h-full flex flex-col items-center justify-center text-gray-500 text-sm">
                    <p>Ask your first question to get insights.</p>
                </div>

                <!-- Messages -->
                <ChatMessage 
                    v-for="(message, index) in messages"
                    :key="index"
                    :message="message.text"
                    :isUser="message.isUser"
                />
            </div>

            <ChatMessage v-if="isThinking" message="AI is analyzing your data..." :isUser="false" />

            <!-- Input Bar -->
            <div class="mt-4 flex gap-3">
                <input 
                    v-model="input" 
                    type="text" 
                    placeholder="AI assistant will be available once backend is connected"
                    class="flex-1 bg-gray-800 border border-gray-700 rounded-lg px-4 py-2 text-sm" 
                    disabled 
                />

                <button class="bg-gray-700 text-gray-400 px-5 rounded-lg text-sm cursor-not-allowed"
                    disabled>
                    Ask
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import ChatMessage from '../components/ChatMessage.vue'

    const messages = ref([
        {
            text: 'How much did I spend on groceries last month?',
            isUser: true,
        },
        {
            text: 'You spent $350 on groceries last month, which is 12% higher than the previous month.',
            isUser: false,
        },
    ])

    const input = ref('')
    const isThinking = ref(false)
</script>