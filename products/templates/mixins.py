class GenericEditViewMixins(object):

    extra_context = None

    def get_context_data(self, **kwargs):
        ctxt = super(GenericEditViewMixins, self).get_context_data(**kwargs)
        ctxt['title'] = self.title
        if self.extra_context is not None:
            ctxt.update(self.extra_context)
        return ctxt

