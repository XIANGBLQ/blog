# Frontend Workflow Toolbox Summary 

- date: 2016-09-18 23:45
- tags: frontend, study
- category: guides
-----------------------------


I'm working my job as a frontend developer currently. So I will do some research and write about the tools I've been using to develop Javasript frontend projects.

### 1. CSS



### 2. Javascript

#### 2.1 Browserify

Uses the same module system as nodejs that can compile, build, and pack javascript modules in node-flavoured CommonJS way for browser. You can manage frontend dependencies with npm, using `require()` method to import, and "module.exports" to export, just like the way nodejs does.

When compiling, browserify will start with an entry file(e.g. './app.js'), then find the whole `abstract syntax tree` of the file by static analysis, and pack all the related content into one files.

In order to make node modules more compatible with browser side, browserify also provides many [builtins modules](https://github.com/substack/browserify-handbook#builtins) such as `events`, `os`, `querystring`, etc.

The best part of browserify is that providing the static analysis and compiling platform, you can also have customized transformers for files other than the standard JS. This enables compiling coffee script or other favors, and also other plugins such as code coverage, in a pipe streaming way. 

In bundling, browserify has two functions: 

1. `ignore`, making a stub definition for some methods only available for node-specific modules
2. ``exclude`, to separate files in different bundle, so don't pack the specific files




Reference: <https://github.com/substack/browserify-handbook#introduction>

#### 2.2 Gulp


If you want to do something quick and dirty, just checkout the Gulp Recipes and copy the the code you want. The Recipes have prepare many examples of small tasks for you to reference.

References:

 - Gulp:  <https://github.com/gulpjs/gulp>
 - Gulp + Browserify Guide: <https://www.viget.com/articles/gulp-browserify-starter-faq>
 - Gulp Recipes: <https://github.com/gulpjs/gulp/tree/master/docs/recipes>
 - Principles of Gulp Plugin: <https://github.com/gulpjs/gulp/blob/master/docs/writing-a-plugin/README.md>

#### 2.3 Babel

The language transfrm platform and the cutting edge of ES(ECMAScript/Javascript) standard. It can transform ES6(ES2015), ES7(ES2016) scripts to compatible ES5. So you can use it as a `transformer` in browserify and compile the files you have written in ES6, etc. The official web site says the main features about it:

 * Babel Presets,
 * Babel Polyfill, new globals such as Promise or new native methods. 
 * JSX and Flow support

References:

 - ES6: <https://github.com/rse/es6-features>
 - Babel: <http://babeljs.io/>
 - Babel Plugins(Presets, Stage-X, and Transform Plugins): <http://babeljs.io/docs/plugins/> 

#### 2.4  Webpack



### 3. Others

#### 3.1 Coffee Script


#### 3,2 Type Script


### 4. Vocabulary

There are some terms in web frontend development that is not meaning obviously, so I collect some of them here.


 * [**Polyfill**](https://en.wikipedia.org/wiki/Polyfill) - a polyfill is cod e that implements a feature on web browsers that do *not* support it. It is a *shim* for a browser API.

 * [**Shim**](https://en.wikipedia.org/wiki/Shim_\(computing\)) - A small library that transparently intercepts API calls. This term can be  commonly used to support an old API in a newer environment, or a new API in an older environment, or running programs on a different platform than they were developed for.

 * [**glob**](https://en.wikipedia.org/wiki/Glob_(programming)) - A pattern that specifies a set of files with wildcard characters. It is originally a program `/etc/glob` that look for files by patterns, then it is used in a lof of libraries in many language. The original word is short for 'global command'.




