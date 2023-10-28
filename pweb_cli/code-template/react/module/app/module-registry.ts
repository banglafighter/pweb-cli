import {_loadTranslation, RapidAppConfig, RapidURLMapping} from "react-rapid-app";
import {BANGLA} from "./locales/bn";
import {ENGLISH} from "./locales/en";


export default class ___REGISTRY_CLASS_NAME___Registry {

    private static loadTranslation() {
        _loadTranslation("en", ENGLISH)
        _loadTranslation("bn", BANGLA)
    }

    public static register(urlMapping: RapidURLMapping, appConfig: RapidAppConfig): void {
        this.loadTranslation()
    }
}