/** @odoo-module **/

import { Component, xml } from "@odoo/owl";

export class MyComponent extends Component {
    static template = xml`
        <div class="bg-info text-center p-2">
            <b> Welcome to Odoo </b>
            <i class="fa fa-close p-1 float-right"
                style="cursor: pointer;"
                t-on-click="onRemove"> </i>
        </div>`;

    onRemove(ev) {
        this.destroy();
    }
}