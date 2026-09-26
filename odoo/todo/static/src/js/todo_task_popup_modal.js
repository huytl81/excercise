/** @odoo-module **/

import { Component, proxy, t, useProps } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class TodoTaskPopupModal extends Component {
    static template = "todo_task_popup_modal";

    props = useProps({
        title: t.string().optional(),
        task: t.object().optional(),
        users: t.array().optional(),
        priorityOptions: t.array().optional(),
        onSave: t.function().optional(),
        close: t.function(),
    });

    setup() {
        this.dialog = useService("dialog");
        
        // Initialize with default values
        const defaultTask = { 
            name: "", 
            user_id: "", 
            is_done: false, 
            priority: "", 
            deadline: "", 
            color: "#000000" 
        };
        
        // Ensure user_id is a string for the select input
        const taskData = this.props.task 
            ? {
                ...defaultTask,
                ...this.props.task,
                user_id: this.props.task.user_id !== undefined && this.props.task.user_id !== null 
                    ? String(this.props.task.user_id) 
                    : ""
            } 
            : defaultTask;
        
        this.state = proxy({
            task: taskData,
            errors: {},
            users: (this.props.users || []).map(user => ({
                ...user,
                id: String(user.id) // Chuyển đổi ID thành chuỗi ngay tại đây
            })),
            priorityOptions: this.props.priorityOptions || []
        });                     
    }

    async onSave(ev) {
        if (ev && ev.preventDefault) {
            ev.preventDefault();
        }
        if (!this.validateForm()) {
            return;
        }
        try {
            if (this.props.onSave) {
                const taskData = {
                    ...this.state.task,
                    user_id: this.state.task.user_id || false
                };
                await this.props.onSave(taskData);
            }
            this.props.close();
        } catch (error) {
            console.error("Error saving task:", error);
        }
    }

    async onCancel(ev) {
        if (ev && ev.preventDefault) {
            ev.preventDefault();
        }
        this.props.close();
    }

    validateForm() {
        const errors = {};
        if (!this.state.task.name || this.state.task.name.trim() === '') {
            errors.name = 'Task name is required';
        }
        this.state.errors = errors;
        return Object.keys(errors).length === 0;
    }
}